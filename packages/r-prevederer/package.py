# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrevederer(RPackage):
	"""Wrapper for the 'Prevedere' API

	Easy and efficient access to the API provided by 'Prevedere', 
  an industry insights and predictive analytics company. Query and 
  download indicators, models and workbenches built with 'Prevedere' for further 
  analysis and reporting <https://www.prevedere.com/>.
	"""
	
	homepage = "https://github.com/wkdavis/prevederer"
	cran = "prevederer" 

	version("0.0.1", md5="1daa7c6b408f1f5ac4c3878b5e4f424c")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
