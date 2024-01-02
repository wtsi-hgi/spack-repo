# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Trust4(MakefilePackage):
    """TRUST4 is a computational tool to analyze TCR and BCR sequences using unselected RNA sequencing data, profiled from fluid and solid tissues, including tumors."""

    homepage = "https://github.com/liulab-dfci/TRUST4"
    url = "https://github.com/liulab-dfci/TRUST4/archive/refs/tags/v1.0.13.tar.gz"

    depends_on("zlib")
    depends_on("pkg-config")

    version("1.0.13", sha256="64069e2cad65960471f32daaf8568c05214b1d8b6b32b7fd138e56b90d634bb8")
    version("1.0.12", sha256="215715de74454e540b7326875b0b76fbf9cbd116bcc0fc71bf0f46ed0e2a7d1d")
    version("1.0.11", sha256="33528e37a893bca6c4451eae6a9f4676b67bae288e7bbb405dc2b9dc8fe7f3ff")
    version("1.0.10", sha256="c469092f0e26dfc8825eb72987f83b7fe3ca82c3f7c7e3e2e3590c90f2208b2a")
    version("1.0.9", sha256="a7e3c7874ca5416e0160a9faca7ee6164473eedc8a0d2390d556ae5759854511")
    version("1.0.8-beta", sha256="980f3d2d3120bcafdb2e3612db3f855c8cacb7e298e38c9f3f96fdb8c33d1d2f")
    version("1.0.8", sha256="87c03829e5e46298d95edcfd2f858a94abf7d3f2a7e16c54e9b7f53a745ae5b4")
    version("1.0.7", sha256="633cab6ef0fa082012ce6a185e818b5454ef16576e9a165f268d69335b3aef5f")
    version("1.0.6", sha256="ebc742a6a1b36ad6b650df22c4f252415d42fd4a9a30e0ce5ab55df91ead46d6")
    version("1.0.5.1", sha256="a77000adb28b0cc6717f568a6b39d6b6f340b04ac3815fc796a1ae672c96b301")

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        for exe in ["annotator", "bam-extractor", "fastq-extractor", "run-trust4", "trust4"]:
            install(exe, prefix.bin)
