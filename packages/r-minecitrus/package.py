# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMinecitrus(RPackage):
	"""Extract and Analyze Median Molecule Intensity from 'citrus'
Output

	Citrus is a computational technique developed for the analysis
    of high dimensional cytometry data sets. This package extracts, statistically
    analyzes, and visualizes marker expression from 'citrus' data. This code was used to 
    generate data for Figures 3 and 4 in the forthcoming manuscript: Throm et al. 
    “Identification of Enhanced Interferon-Gamma Signaling in Polyarticular Juvenile 
    Idiopathic Arthritis with Mass Cytometry”, JCI-Insight. For more information on Citrus,
    please see: Bruggner et al. (2014) <doi:10.1073/pnas.1408792111>. To download
    the 'citrus' package, please see <https://github.com/nolanlab/citrus>. 
	"""
	
	cran = "mineCitrus" 

	version("1.0.0", md5="6e28378f44485732ec4afffe2eebce34")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
