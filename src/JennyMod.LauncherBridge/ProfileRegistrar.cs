using System;
using System.IO;
using System.Text.Json;
using System.Text.Json.Nodes;

namespace JennyMod.LauncherBridge;

/// <summary>Registers the "JennyMod (Fabric)" profile in launcher_profiles.json.</summary>
public static class ProfileRegistrar
{
    public const string ProfileName = "JennyMod (Fabric)";

    public static bool EnsureProfile(string minecraftDir, string mcVersion)
    {
        var path = Path.Combine(minecraftDir, "launcher_profiles.json");
        if (!File.Exists(path)) return false;

        var root = JsonNode.Parse(File.ReadAllText(path))!.AsObject();
        var profiles = root["profiles"]?.AsObject();
        if (profiles is null) return false;

        foreach (var kv in profiles)
        {
            if (kv.Value?["name"]?.GetValue<string>() == ProfileName) return false;
        }

        var key = Guid.NewGuid().ToString("N")[..16];
        profiles[key] = new JsonObject
        {
            ["name"] = ProfileName,
            ["lastVersionId"] = $"fabric-loader-0.15.7-{mcVersion}",
            ["type"] = "custom"
        };

        File.WriteAllText(path, root.ToJsonString(new JsonSerializerOptions { WriteIndented = true }));
        return true;
    }
}