# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RGsmr(RPackage):
    """The gsmr R-package implements the GSMR (Generalised Summary-data-based Mendelian Randomisation) method that uses GWAS summary statistics to test for a putative causal association between two phenotypes (e.g., a modifiable risk factor and a disease) based on a multi-SNP model (Zhu et al. 2018 Nature Communications)."""

    homepage = "https://yanglab.westlake.edu.cn/software/gsmr/"
    url = "https://yanglab.westlake.edu.cn/software/gsmr/static/gsmr_1.1.1.tar.gz"

	version("1.1.1", sha256="999bc6e894780dde20eb1f596ce97d7f99973e6399c8c54353e72555af5e7718")

    depends_on("r-markdown", type=("build", "run"))
    depends_on("r-survey", type=("build", "run"))
