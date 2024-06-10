# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install pbmm2
#
# You can edit this file again by typing:
#
#     spack edit pbmm2
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Pbmm2(MesonPackage):
    """A minimap2 SMRT wrapper for PacBio data: native PacBio data in ⇨ native PacBio BAM out.

    pbmm2 is a SMRT C++ wrapper for minimap2's C API. Its purpose is to support native PacBio
    in- and output, provide sets of recommended parameters, generate sorted output on-the-fly,
    and postprocess alignments. Sorted output can be used directly for polishing using GenomicConsensus,
    if BAM has been used as input to pbmm2. Benchmarks show that pbmm2 outperforms BLASR in
    sequence identity, number of mapped bases, and especially runtime. pbmm2 is the official
    replacement for BLASR.
    """

    homepage = "https://github.com/PacificBiosciences/pbmm2"
    url = "https://github.com/PacificBiosciences/pbmm2/archive/refs/tags/v1.13.1.tar.gz"

    license("BSD-3-Clause-Clear license")

    version("1.13.1", sha256="7baf2608cbf05454e3d1693143695d22ed4aba72b4f11d5bc168d6d2be4b304a")

    depends_on("zlib-api", type=("build", "run"))
    depends_on("boost", type=("build", "run"))
    depends_on("htslib@1.7:", type=("build", "run"))
    depends_on("pbbam", type=("build", "run"))
    depends_on("pbcopper", type=("build", "run"))
    depends_on("pbminimap2", type=("build", "run"))
    depends_on("cmake", type="build")

    def meson_args(self):
        return ["-Dtests=false"]

    # def setup_build_environment(self, env):
    #     env.prepend_path("PKG_CONFIG_PATH", join_path(self.spec["minimap2"].prefix, "lib", "pkgconfig"))
