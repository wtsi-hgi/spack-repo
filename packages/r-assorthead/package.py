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
#     spack install r-assorthead
#
# You can edit this file again by typing:
#
#     spack edit r-assorthead
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class RAssorthead(RPackage):
    """Assorted Header-Only C++ Libraries.

    Vendors an assortment of useful header-only C++ libraries. Bioconductor 
    packages can use these libraries in their own C++ code by LinkingTo this 
    package without introducing any additional dependencies. The use of a central 
    repository avoids duplicate vendoring of libraries across multiple R packages, 
    and enables better coordination of version updates across cohorts of 
    interdependent C++ libraries."""

    homepage = "https://github.com/LTLA/assorthead"
    url = "https://bioconductor.org/packages/release/bioc/src/contrib/assorthead_1.0.1.tar.gz"
    bioc = "assorthead"

    maintainers("LTLA")

    license("MIT")

    version("1.0.1", sha256="98f535b69165bb2b0c7c5bc67e412ceccb3c78ac19fe7580254a5a97028791d5")

    # Suggests
    depends_on("r-knitr", type=("build"))
    depends_on("r-rmarkdown", type=("build"))
    depends_on("r-biocstyle", type=("build"))

    def configure_args(self):
        # FIXME: Add arguments to pass to install via --configure-args
        # FIXME: If not needed delete this function
        args = []
        return args
