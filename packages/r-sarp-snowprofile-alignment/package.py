# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSarpSnowprofileAlignment(RPackage):
	"""Snow Profile Alignment, Aggregation, and Clustering

	Snow profiles describe the vertical (1D) stratigraphy of layered 
    snow with different layer characteristics, such as grain type, hardness, 
    deposition date, and many more. Hence, they represent a data format similar 
    to multivariate time series containing categorical, ordinal, and numerical 
    data types. Use this package to align snow profiles by matching their 
    individual layers based on Dynamic Time Warping (DTW). The aligned profiles 
    can then be assessed with an independent, global similarity measure that is 
    geared towards avalanche hazard assessment. Finally, through exploiting data
    aggregation and clustering methods, the similarity measure provides the
    foundation for grouping and summarizing snow profiles according to similar
    hazard conditions. In particular, this package allows for averaging large
    numbers of snow profiles with DTW Barycenter Averaging and thereby 
    facilitates the computation of individual layer distributions and summary 
    statistics that are relevant for avalanche forecasting purposes. 
    For more background information refer to Herla, Horton, Mair,
    and Haegeli (2021) <doi:10.5194/gmd-14-239-2021>, and Herla, Mair, and Haegeli 
    (2022) <doi:10.5194/tc-16-3149-2022>.
	"""
	
	homepage = "https://avalancheresearch.ca/"
	cran = "sarp.snowprofile.alignment" 

	version("1.2.2", md5="214a065eff02c2d995823da24c4f4ba1")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-sarp-snowprofile@1.2.1:", type=("build", "run"))
	depends_on("r-dtw", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
