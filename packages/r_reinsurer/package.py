# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReinsurer(RPackage):
	"""Reinsurance Treaties Application

	Application of reinsurance treaties to claims portfolios. 
            The package creates a class Claims whose objective is to 
            store claims and premiums, on which different treaties can be applied.
            A statistical analysis can then be applied to measure the impact of
            reinsurance, producing a table or graphical output. This package can
            be used for estimating the impact of reinsurance on several portfolios
            or for pricing treaties through statistical analysis. Documentation
            for the implemented methods can be found in "Reinsurance: Actuarial
            and Statistical Aspects" by Hansjöerg Albrecher, Jan Beirlant,
            Jozef L. Teugels (2017, ISBN: 978-0-470-77268-3) and 
            "REINSURANCE: A Basic Guide to Facultative and Treaty Reinsurance"
            by Munich Re (2010) <https://www.munichre.com/site/mram/get/documents_E96160999/mram/assetpool.mr_america/PDFs/3_Publications/reinsurance_basic_guide.pdf>.
	"""
	
	cran = "reinsureR" 

	version("0.1.0", md5="929313d01032d95558ae774e1a2b2dd6")

	depends_on("r@2.2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
