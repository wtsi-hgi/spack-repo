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
#     spack install r-ldlinkr
#
# You can edit this file again by typing:
#
#     spack edit r-ldlinkr
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class RLdlinkr(RPackage):
    """Provides access to the 'LDlink' API (<https://ldlink.nih.gov/?tab=apiaccess>) using the R console. This programmatic access facilitates researchers who are interested in performing batch queries in 1000 Genomes Project (2015) <doi:10.1038/nature15393> data using 'LDlink'. 'LDlink' is an interactive and powerful suite of web-based tools for querying germline variants in human population groups of interest. For more details, please see Machiela et al. (2015) <doi:10.1093/bioinformatics/btv402>."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://cran.r-project.org/web/packages/LDlinkR/vignettes/LDlinkR.html"
    cran = "LDlinkR"

    license("GPL-2, GPL-3")

    version("1.4.0", sha256="b25380a0897aebe0004ed933e1936c4bc2dcd4fb769417134ac31acdbd373229")
    version("1.3.0", sha256="81dbe6817b6bab6c44f1d34f509123e0242360348285d5377624bc831b33832a")
    version("1.2.3", sha256="3cbe6aee8c8657b63bde27cb9e2fe20e96694f47dbbb8ada98d33128c18179d1")
    version("1.2.2", sha256="4ac0a865a87c33662a532f30ac51587dcf8b9c3dc95cd6f76978f79a0a21c47f")
    version("1.2.1", sha256="d87c0b3ab2565c11e060cbc5c94e17f9eaa18d142ad122e7ef33d0327f197f89")
    version("1.2.0", sha256="b83d5230cab42f5973bd3986f2edcc2f720685f3fa99003063719df71fd68e23")
    version("1.1.2", sha256="ef23b6c0219606d77785d277de3a6e0c698aa2053cbb7956ce537fa549ddcab1")
    version("1.1.1", sha256="e125282a0e568c7f65568a6bae0f5b036961e243e7379d3069165bf0d1df3283")
    version("1.0.2", sha256="f040dafee534f7a9828ad8fb3a582ff20a760f79a678faacd358520603798304")
    version("1.0.1", sha256="3399c30c4ebc5ede4b5f7d80427d5215cc4667043f75334897576887ce3fefcc")
    version("1.0.0", sha256="b578f43e15117efbd2433fdee7719604b5eb714809ce069b4b560e348fe91cc6")

    depends_on("r-httr", type=("build", "run"))
    depends_on("r-r-utils", type=("build", "run"))
