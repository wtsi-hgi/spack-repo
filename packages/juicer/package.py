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
#     spack install juicer
#
# You can edit this file again by typing:
#
#     spack edit juicer
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Juicer(Package):
    """Juicer is a platform for analyzing kilobase resolution Hi-C data.
    It includes the pipeline for generating Hi-C maps from fastq raw data files
    and command line tools for feature annotation on the Hi-C maps."""

    homepage = "https://github.com/aidenlab/juicer"
    url = "https://github.com/aidenlab/juicer/archive/refs/tags/1.6.tar.gz"

    license("MIT")

    version("1.6", sha256="cef7783a2ddfbacbf4b229f6a4e236c534780b6bb4ec7f84fe8497cd6e57d3b0")

    depends_on("java@1.8:", type=("build", "run", "link"))
    depends_on("bwa")
    depends_on("cuda@8")
    depends_on("python", type=("build", "run"))
    depends_on("coreutils")
    depends_on("juicertools")
    depends_on("libxrender")
    depends_on("libxtst")
    depends_on("libxi")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install_tree("CPU", prefix.bin)

    def setup_run_environment(self, env):
        # Add libxrender to LD_LIBRARY_PATH
        for x_dep in ["libxrender", "libxtst", "libxi"]:
            env.prepend_path("LD_LIBRARY_PATH", self.spec[x_dep].prefix.lib)
