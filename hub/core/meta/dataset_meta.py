from typing import Any, Dict
from hub.core.meta.meta import Meta


class DatasetMeta(Meta):
    def __init__(self):
        super().__init__()
        self.tensors = []
        self.groups = []
        self.info_updated = False

    @property
    def nbytes(self):
        # TODO: can optimize this
        return len(self.tobytes())

    def __getstate__(self) -> Dict[str, Any]:
        d = super().__getstate__()
        d["tensors"] = self.tensors
        d["groups"] = self.groups
        d["info_updated"] = self.info_updated
        return d

    def __setstate__(self, state: Dict[str, Any]):
        self.tensors = state["tensors"]
        self.groups = state["groups"]
        self.info_updated = state.get("info_updated", False)

    def add_tensor(self, name):
        if name not in self.tensors:
            self.tensors.append(name)
            self.is_dirty = True

    def add_group(self, name):
        if name not in self.groups:
            self.groups.append(name)
            self.is_dirty = True

    def delete_tensor(self, name):
        self.tensors.remove(name)
        self.is_dirty = True

    def delete_group(self, name):
        self.groups = list(filter(lambda g: not g.startswith(name), self.groups))
        self.tensors = list(filter(lambda t: not t.startswith(name), self.tensors))
        self.is_dirty = True

    def modify_info(self) -> None:
        """Stores information that the info has changed"""
        self.info_updated = True
        self.is_dirty = True
