# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCatencoders(RPackage):
	"""Encoders for Categorical Variables

	Contains some commonly used categorical variable encoders, such as 'LabelEncoder' and 'OneHotEncoder'. Inspired by the encoders implemented in Python 'sklearn.preprocessing' package (see <http://scikit-learn.org/stable/modules/preprocessing.html>).
	"""
	
	cran = "CatEncoders" 

	version("0.1.1", md5="7f506add6948594bcf6a83e4fc5881b2")

	depends_on("r-matrix@1.2.6:", type=("build", "run"))
	depends_on("r-data-table@1.9.6:", type=("build", "run"))
