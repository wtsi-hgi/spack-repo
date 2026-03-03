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
#     spack install r-lcv
#
# You can edit this file again by typing:
#
#     spack edit r-lcv
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class RLcv(RPackage):
    """LCV is a method for inferring genetically causal relationships using GWAS data.

    LCV is implemented in Matlab and R. In order to run LCV, you will need LD scores (non-stratified, with ancestry matching your GWAS data), which can be downloaded here. You can also compute your own LD scores using the LDSC software. You will also need signed summary statistics: either effect size estimates (in units of per-normalized-genotype effect size) or Z scores.

    Usage of each function is described within the source code. There are example simulation scripts in Matlab and R, and an example script to run on real data in R.
    """

    homepage = "https://github.com/lukejoconnor/LCV"
    git = "https://github.com/lukejoconnor/LCV.git"

    version("20200630", commit="39950a8b9c67d812a5f7ec8a1df6951942cb258e")

    def patch(self):
        with open("NAMESPACE", "w") as f:
            f.write('exportPattern( "." )')

        with open("DESCRIPTION", "w") as f:
            f.write("""Package: LCV
Type: Package
Title: LCV: Inferring Genetically Causal Relationships Using GWAS Data
Version: 1.0
Author: Luke J. O'Connor [aut, cre]
Description: LCV is a method for inferring genetically causal relationships using GWAS data.
Depends: R (>= 2.15.0)
""")

        remove("R/ExampleRealdataScript.R")
        remove("R/ExampleSimulationScript.R")
