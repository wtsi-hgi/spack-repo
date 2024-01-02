# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Vartrix(Package):
    """VarTrix is a software tool for extracting single cell variant information from 10x Genomics single cell data. VarTrix will take a set of previously defined variant calls and use that to identify those variants in the single cell data. VarTrix does not perform variant calling. VarTrix is useful for evaluating heterogeneity within a sample, which means that the types of variants that will be useful are either somatic or contained within a copy number variant (CNV) event."""

    homepage = "https://github.com/10XGenomics/vartrix"
    url = "https://github.com/10XGenomics/vartrix/archive/refs/tags/v1.1.22.tar.gz"

    version("1.1.22", sha256="2ccb5dfdf3b0ee0cb149d181229177fa29b7820f5b77c772014ca32d53df5523")
    version("1.1.20", sha256="d755c318de80e4e88024730e12e066376eb56ec8d8762855936d7cdcf8cb2a2a")
    version("1.1.19", sha256="6bfdd5cb70f0a33fa5fd6048370b266ecd92f3c5f7a6a4ad39f724f9c3558487")
    version("1.1.18", sha256="12d8c9a05deeab7746fe0ff800dc27ef80fac3703ddf4287c5774be4d935a95a")
    version("1.1.16", sha256="f79961387540523201bff5baa59a983fcc5ff1f7c26c1428cc04bb715bcc611b")
    version("1.1.15", sha256="fb19e5055fd61428335717926386b8a19b26f86c93f56e41b2db8e99583bcae2")
    version("1.1.14", sha256="eeee5d5c98f9e054cc5f150ac04deff3626a62b89d237f1c069dc7ad5205ac38")
    version("1.1.13", sha256="985af4b76ba6a1fd7c9bbc84763f470992cd3ec24df6868dd9c18659fda45dcc")
    version("1.1.12", sha256="e13bfe02905b1ee978aeb55be0cb2447caf7139ce997860065eaf72dc06330e1")
    version("1.1.11", sha256="df55a739f93ab17a2c81309c8f7fc563fbcfe4a8545be871c671741c28e26a23")

    depends_on("rust", type="build")

    def install(self, spec, prefix):
        cargo = which("cargo")

        cargo("build", "--release")

        install("target/release/vartrix", prefix.bin)

    def setup_run_environment(self, env):
        env.prepend_path("PATH", self.prefix.bin)
