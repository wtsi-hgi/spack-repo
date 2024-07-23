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
#     spack install eigensoft
#
# You can edit this file again by typing:
#
#     spack edit eigensoft
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Eigensoft(MakefilePackage):
    """The EIGENSOFT package implements methods from the following 2 papers:
    Patterson et al. 2006 PLoS Genet 2:e190 (population structure)
    Price et al. 2006 Nat Genet 38:904-9 (EIGENSTRAT stratification correction)
    """

    homepage = "https://github.com/DReichLab/EIG"
    url = "https://github.com/DReichLab/EIG/archive/refs/tags/v8.0.0.tar.gz"

    version("8.0.0", sha256="e3459e8ac0134da369910454854eae5c7b261e8816318ccbd2d371b4c6c35741")

    depends_on("gsl")
    depends_on("lapack")
    depends_on("openblas")

    def build(self, spec, prefix):
        cd("src")
        make()
        make("install")

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install_tree(self.stage.source_path + "/bin", prefix.bin)
