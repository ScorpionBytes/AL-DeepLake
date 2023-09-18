#include <gtest/gtest.h>
#include <filesystem>
#include <nlohmann/json.hpp>
#include "../../../deeplog/actions/protocol_action.hpp"

using json = nlohmann::json;


TEST(ActionTest, UpgradeProtocolJson) {

    auto orig = deeplog::protocol_action(5, 6);

    json j = json::object();
    orig.to_json(j);

    EXPECT_EQ("{\"protocol\":{\"minReaderVersion\":5,\"minWriterVersion\":6}}", j.dump());

    auto parsed = deeplog::protocol_action(j);
    EXPECT_EQ(5, parsed.min_reader_version());
    EXPECT_EQ(6, parsed.min_writer_version());
}

