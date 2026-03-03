# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDdi(RPackage):
	"""The Data Defect Index for Samples that May not be IID

	Implements Meng's data defect index (ddi), which represents
    the degree of sample bias relative to an iid sample. The data defect 
    correlation (ddc) represents the correlation between the outcome of interest
    and the selection into the sample; when the sample selection is independent
    across the population, the ddc is zero. Details are in Meng (2018) 
    <doi:10.1214/18-AOAS1161SF>, "Statistical Paradises and Paradoxes in Big Data (I): 
    Law of Large Populations, Big Data Paradox, and the 2016 US Presidential 
    Election." Survey estimates from the Cooperative Congressional Election Study 
    (CCES) is included to replicate the article's results. 
	"""
	
	homepage = "https://github.com/kuriwaki/ddi"
	cran = "ddi" 

	version("0.1.0", md5="e5e6669c1893645916136d01e6148c52")

	depends_on("r@2.10:", type=("build", "run"))
