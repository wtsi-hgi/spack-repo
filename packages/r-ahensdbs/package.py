# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAhensdbs(RPackage):
    """EnsDbs for AnnotationHub

    Supplies AnnotationHub with EnsDb Ensembl-based annotation databases for all species. EnsDb SQLite databases are generated separately from Ensembl MySQL databases using functions from the ensembldb package employing the Ensembl Perl API.
    """

    bioc = "AHEnsDbs"

    version("1.7.0", commit="2cef9f0b74c7f617665788875b2f36205083b181")
    version("1.1.11", commit="c46268659af7e572fded8298ba87ba29189a594a")

    depends_on("r@3.4:", type=("build", "run"))
    depends_on("r-ensembldb@1.99.10:", type=("build", "run"))
    depends_on("r-annotationhubdata@1.5.24:", type=("build", "run"))
