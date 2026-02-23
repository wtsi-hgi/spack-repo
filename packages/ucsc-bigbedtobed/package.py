# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class UcscBigbedtobed(Package):
    """Convert from bigBed to ASCII BED format."""

    homepage = "https://hgdownload.cse.ucsc.edu/admin/exe"
    url = "https://hgdownload.cse.ucsc.edu/admin/exe/userApps.archive/userApps.v482.src.tgz"

    version("482", sha256="745d0f0a980e9f863373b0b0a6ad7961a1d0f53a9d7c446e92fc28fc4909431a")

    depends_on("cmake@3.6:")
    depends_on("gmake")
    depends_on("libpng")
    depends_on("libuuid")
    depends_on("openssl")
    depends_on("zlib-api")
    depends_on("bzip2")
    depends_on("xz")
    depends_on("libiconv")
    depends_on("mariadb-c-client")

    def setup_build_environment(self, env):
        env.set("MYSQLLIBS", "-lmysqlclient")
        env.set("L", "-lssl")
        env.set("BINDIR", "bin")

    def install(self, spec, prefix):
        build_dirs = [
            "kent/src/lib",
            "kent/src/htslib",
            "kent/src/jkOwnLib",
            "kent/src/hg/lib",
        ]

        for relpath in build_dirs:
            with working_dir(relpath):
                make()

        with working_dir("kent/src/utils/bigBedToBed"):
            mkdirp("bin")
            mkdirp(prefix.bin)
            make()
            make("install")
            install("bin/bigBedToBed", prefix.bin)

        sample_dir = join_path(prefix.share, "ucsc-bigbedtobed")
        mkdirp(sample_dir)
        install(
            join_path(
                self.stage.source_path,
                "kent",
                "src",
                "utils",
                "bigGuessDb",
                "tests",
                "in",
                "hg19.bb",
            ),
            sample_dir,
        )

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            sample = join_path(self.prefix.share, "ucsc-bigbedtobed", "hg19.bb")
            big_bed_to_bed = Executable(join_path(self.prefix.bin, "bigBedToBed"))
            big_bed_to_bed(sample, "converted.bed")
