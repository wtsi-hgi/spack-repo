# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpm(RPackage):
	"""Spatial Predictive Modeling

	Introduction to some novel accurate hybrid methods of geostatistical and machine learning methods for spatial predictive modelling. It contains two commonly used geostatistical methods, two machine learning methods, four hybrid methods and two averaging methods. For each method, two functions are provided. One function is for assessing the predictive errors and accuracy of the method based on cross-validation. The other one is for generating spatial predictions using the method. For details please see: Li, J., Potter, A., Huang, Z., Daniell, J. J. and Heap, A. (2010) <https:www.ga.gov.au/metadata-gateway/metadata/record/gcat_71407>
  Li, J., Heap, A. D., Potter, A., Huang, Z. and Daniell, J. (2011) <doi:10.1016/j.csr.2011.05.015>
  Li, J., Heap, A. D., Potter, A. and Daniell, J. (2011) <doi:10.1016/j.envsoft.2011.07.004>
  Li, J., Potter, A., Huang, Z. and Heap, A. (2012) <https:www.ga.gov.au/metadata-gateway/metadata/record/74030>.
	"""
	
	cran = "spm" 

	version("1.2.2", md5="3df9678b6ddc49b198fe63aa068f19a1")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-gstat", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-psy", type=("build", "run"))
	depends_on("r-gbm", type=("build", "run"))
	depends_on("r-biomod2", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
