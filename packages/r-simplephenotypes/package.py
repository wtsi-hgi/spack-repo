# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimplephenotypes(RPackage):
	"""Simulation of Pleiotropic, Linked and Epistatic Phenotypes

	The number of studies involving correlated traits and the availability of tools to handle this type of data has increased considerably in the last decade. With such a demand, we need tools for testing hypotheses related to single and multi-trait (correlated) phenotypes based on many genetic settings. Thus, we implemented various options for simulation of pleiotropy and Linkage Disequilibrium under additive, dominance and epistatic models. The simulation currently takes a marker data set as an input and then uses it for simulating multiple traits as described in Fernandes and Lipka (2020) <doi:10.1186/s12859-020-03804-y>.
	"""
	
	homepage = "https://github.com/samuelbfernandes/simplePHENOTYPES"
	cran = "simplePHENOTYPES" 

	version("1.3.0", md5="534a84f2e9a22335779de1207d058269")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-snprelate", type=("build", "run"))
	depends_on("r-gdsfmt", type=("build", "run"))
