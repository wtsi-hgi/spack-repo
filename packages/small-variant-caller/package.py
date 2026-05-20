from spack.package import *


class SmallVariantCaller(Package):
    """Roche small variant caller for SBX data.

    Small Variant Caller (SVC) filters and re-genotypes candidate small
    variants generated from SBX data workflows and also ships companion tools
    for feature generation and model training.
    """

    homepage = "https://github.com/Roche-AXELIOS/XOOS/tree/main/small_variant_caller"
    url = "https://github.com/Roche-AXELIOS/XOOS/archive/refs/tags/0.80.0.tar.gz"

    license("Apache-2.0")

    version(
        "0.80",
        sha256="f68d81c48c036182b77bafa27ca2cd589d70063c4120372daf73f96e4a1245e5",
        url="https://github.com/Roche-AXELIOS/XOOS/archive/refs/tags/0.80.0.tar.gz",
    )

    depends_on("curl", type="build")
    depends_on("tar", type="build")

    def install(self, spec, prefix):
        image = "ghcr.io/roche-axelios/xoos/small_variant_caller:0.80"
        manifest = join_path(self.stage.path, "manifest.json")

        curl = which(spec["curl"].prefix.bin.curl)
        tar = which(spec["tar"].prefix.bin.tar)

        token = Executable("bash")
        token_output = token(
            "-lc",
            "curl -fsSL 'https://ghcr.io/token?service=ghcr.io&scope=repository:roche-axelios/xoos/small_variant_caller:pull' "
            "| python3 -c 'import sys, json; print(json.load(sys.stdin)[\"token\"])'",
            output=str,
        ).strip()

        curl(
            "-fsSL",
            "-H",
            "Authorization: Bearer {0}".format(token_output),
            "-H",
            "Accept: application/vnd.docker.distribution.manifest.v2+json",
            "https://ghcr.io/v2/roche-axelios/xoos/small_variant_caller/manifests/0.80",
            "-o",
            manifest,
        )

        import json

        with open(manifest, encoding="utf-8") as fh:
            data = json.load(fh)

        stage_root = join_path(self.stage.path, "image-root")
        mkdirp(stage_root)

        for layer in data["layers"]:
            digest = layer["digest"]
            safe_digest = digest.replace(":", "-") + ".tar.gz"
            archive = join_path(self.stage.path, safe_digest)
            curl(
                "-fsSL",
                "-H",
                "Authorization: Bearer {0}".format(token_output),
                "https://ghcr.io/v2/roche-axelios/xoos/small_variant_caller/blobs/{0}".format(digest),
                "-o",
                archive,
            )
            tar("-xzf", archive, "-C", stage_root)

        mkdirp(prefix.bin)
        mkdirp(prefix.share.small_variant_caller)

        for exe in [
            "compute_bam_features",
            "compute_vcf_features",
            "filter_variants",
            "train_model",
            "vcf_to_bed",
        ]:
            install(join_path(stage_root, "apps", exe), prefix.bin)

        install_tree(
            join_path(stage_root, "resources"),
            join_path(prefix.share.small_variant_caller, "resources"),
        )

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            filter_variants = which(join_path(self.prefix.bin, "filter_variants"))
            filter_variants("--help")
