# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHandyfunctions(RPackage):
	"""Useful Functions for Handfully Manipulating and Analyzing Data
with Data.frame Format

	Some useful functions for simply manipulating and analyzing data with data.frame format.
  It mainly includes the following sections: ReformatDataframe (reformat dataframe with the modifiers), InteractDataframe, and Post-VCF (for downstream analysis for data generated from 'vcftools' Petr et al (2011) <doi:10.1093/bioinformatics/btr330>
  or 'plink' Chang et al (2015) <doi:10.1186/s13742-015-0047-8>.
	"""
	
	homepage = "https://github.com/LuffyLouis/handyFunctions"
	cran = "handyFunctions" 

	version("0.1.0", md5="313506bbc04566d5d44532f711ad32f8")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr@1:", type=("build", "run"))
