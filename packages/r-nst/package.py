# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNst(RPackage):
	"""Normalized Stochasticity Ratio

	To estimate ecological stochasticity in community assembly. Understanding the community assembly mechanisms controlling biodiversity patterns is a central issue in ecology. Although it is generally accepted that both deterministic and stochastic processes play important roles in community assembly, quantifying their relative importance is challenging. The new index, normalized stochasticity ratio (NST), is to estimate ecological stochasticity, i.e. relative importance of stochastic processes, in community assembly. With functions in this package, NST can be calculated based on different similarity metrics and/or different null model algorithms, as well as some previous indexes, e.g. previous Stochasticity Ratio (ST), Standard Effect Size (SES), modified Raup-Crick metrics (RC). Functions for permutational test and bootstrapping analysis are also included. Previous ST is published by Zhou et al (2014) <doi:10.1073/pnas.1324044111>. NST is modified from ST by considering two alternative situations and normalizing the index to range from 0 to 1 (Ning et al 2019) <doi:10.1073/pnas.1904623116>. A modified version, MST, is a special case of NST, used in some recent or upcoming publications, e.g. Liang et al (2020) <doi:10.1016/j.soilbio.2020.108023>. SES is calculated as described in Kraft et al (2011) <doi:10.1126/science.1208584>. RC is calculated as reported by Chase et al (2011) <doi:10.1890/ES10-00117.1> and Stegen et al (2013) <doi:10.1038/ismej.2013.93>. Version 3 added NST based on phylogenetic beta diversity, used by Ning et al (2020) <doi:10.1038/s41467-020-18560-z>.
	"""
	
	homepage = "https://github.com/DaliangNing/NST"
	cran = "NST" 

	version("3.1.10", md5="08691ed20bf29e7bd8db639e99270571")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-permute", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-bigmemory", type=("build", "run"))
	depends_on("r-icamp", type=("build", "run"))
	depends_on("r-dirichletreg", type=("build", "run"))
