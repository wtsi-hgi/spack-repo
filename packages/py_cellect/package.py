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
#     spack install py-cellect
#
# You can edit this file again by typing:
#
#     spack edit py-cellect
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyCellect(Package):
    """CELL-type Expression-specific integration for Complex Traits (CELLECT) is a computational toolkit for identifing likely etiologic cell-types underlying complex traits. CELLECT leverages existing genetic prioritization models to integrate single-cell transcriptomic and human genetic data when identifing likely etiologic cell-types."""

    homepage = "https://github.com/perslab/CELLECT"
    git = "https://github.com/perslab/CELLECT.git"

    license("GPL-3")

    version("1.3.0", tag="v.1.3.0", submodules=True)

    depends_on("ctg-magma")
    depends_on("python@2.7", type=("build", "run"))
    depends_on("py-pybedtools@0.7", type=("build", "run"))
    depends_on("py-numpy@:1.16", type=("build", "run"))
    depends_on("py-pandas@:0.24", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-bitarray@0.8", type=("build", "run"))
    depends_on("py-nose", type=("build", "run"))

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        mkdirp(prefix.ldsc)
        filter_file("#!/usr/bin/env python", "#!" + self.spec["python"].prefix.bin.python, "ldsc/ldsc.py", string=True)
        install("*.snakefile", prefix)
        install("config.yml", prefix)
        install("ldsc/ldsc.py", join_path(prefix.bin, "ldsc.py"))
        install_tree("ldsc", prefix.ldsc)

    def setup_run_environment(self, env):
        env.prepend_path("PYTHONPATH", self.prefix.ldsc)
