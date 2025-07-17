# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAbarray(RPackage):
    """Microarray QA and statistical data analysis for Applied Biosystems Genome Survey Microrarray (AB1700) gene expression data.

    Automated pipline to perform gene expression analysis for Applied Biosystems Genome Survey Microarray (AB1700) data format. Functions include data preprocessing, filtering, control probe analysis, statistical analysis in one single function. A GUI interface is also provided. The raw data, processed data, graphics output and statistical results are organized into folders according to the analysis settings used.
    """

    bioc = "ABarray"

    version("1.76.0", commit="c9f2673188a8d710bb44dbaf3b226fc8a6529f11")
    version("1.70.0", commit="fdda0b24c0b81a0b7fecacacae412b2bf94508d6")

    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-multtest", type=("build", "run"))
