# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProteasy(RPackage):
    """Protease Mapping

    Retrieval of experimentally derived protease- and cleavage data derived from the MEROPS database. Proteasy contains functions for mapping peptide termini to known sites where a protease cleaves. This package also makes it possible to quickly look up known substrates based on a list of (potential) proteases, or vice versa - look up proteases based on a list of substrates.
    """

    homepage = "https://github.com/martinry/proteasy"
    bioc = "proteasy"

    version("1.4.0", commit="fb6e72dfe743b73d3786eab5ea59d2f8e7dbb6f4")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-ensembldb", type=("build", "run"))
    depends_on("r-annotationfilter", type=("build", "run"))
    depends_on("r-ensdb-hsapiens-v86", type=("build", "run"))
    depends_on("r-ensdb-mmusculus-v79", type=("build", "run"))
    depends_on("r-ensdb-rnorvegicus-v79", type=("build", "run"))
    depends_on("r-rcpi", type=("build", "run"))
