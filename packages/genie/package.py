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
#     spack install genie
#
# You can edit this file again by typing:
#
#     spack edit genie
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Genie(CMakePackage):
    """Gene-ENviroment Interaction Estimator"""

    homepage = "https://github.com/sriramlab/GENIE"
    url = "https://github.com/sriramlab/GENIE/archive/refs/tags/v.1.0.0.tar.gz"
    git = "https://github.com/sriramlab/GENIE.git"

    license("MIT")

    # The version 1.0.1 does not exist, but multiple phenotype function for
    # the python package py-rhe is missing from the 1.0.0 release
    version("1.0.1", commit="aff7617e188f02fec6f86aa51a539bf8a1a4b720")

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install(self.build_directory + "/GENIE", prefix.bin.GENIE)
        install(self.build_directory + "/GENIE_mem", prefix.bin.GENIE_mem)
        install(self.build_directory + "/GENIE_multi_pheno", prefix.bin.GENIE_multi_pheno)
