# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPullword(RPackage):
	"""R Interface to Pullword Service

	R Interface to Pullword Service for natural language processing
    in Chinese. It enables users to extract valuable words from text by deep learning models. 
    For more details please visit the official site (in Chinese) <http://www.pullword.com/>.
	"""
	
	cran = "pullword" 

	version("0.3", md5="b337ba0a2efbf67ca8cb82a8c2db4d32")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
