# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmassbank(RPackage):
    """Workflow to process tandem MS files and build MassBank records

    Workflow to process tandem MS files and build MassBank records. Functions include automated extraction of tandem MS spectra, formula assignment to tandem MS fragments, recalibration of tandem MS spectra with assigned fragments, spectrum cleanup, automated retrieval of compound information from Internet databases, and export to MassBank records.
    """

    bioc = "RMassBank"

    version("3.18.0", commit="a6e88ed0f2f17f1ba4a958b4559cd8ab149d7394")
    version("3.12.0", commit="0a05d667ddc09a01885c612601df11cce90205a4")

    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-xml", type=("build", "run"))
    depends_on("r-rjson", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-digest", type=("build", "run"))
    depends_on("r-rcdk", type=("build", "run"))
    depends_on("r-yaml", type=("build", "run"))
    depends_on("r-mzr", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-msnbase", type=("build", "run"))
    depends_on("r-httr", type=("build", "run"))
    # RMassBank >= 3.x requires modern HTTP and data reading helpers
    depends_on("r-httr2", type=("build", "run"))
    depends_on("r-readr", type=("build", "run"))
    depends_on("r-envipat", type=("build", "run"))
    depends_on("r-assertthat", type=("build", "run"))
    depends_on("r-logger", type=("build", "run"))
    depends_on("r-readjdx", type=("build", "run"))
    depends_on("r-webchem", type=("build", "run"))
    depends_on("r-chemminer", type=("build", "run"))
    depends_on("r-chemmineob", type=("build", "run"))
    depends_on("r-r-utils", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-glue", type=("build", "run"))
    depends_on("openbabel", type=("build", "link", "run"))
