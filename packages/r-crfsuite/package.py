# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrfsuite(RPackage):
	"""Conditional Random Fields for Labelling Sequential Data in
Natural Language Processing

	Wraps the 'CRFsuite' library <https://github.com/chokkan/crfsuite> allowing users 
    to fit a Conditional Random Field model and to apply it on existing data.
    The focus of the implementation is in the area of Natural Language Processing where this R package allows you to easily build and apply models 
    for named entity recognition, text chunking, part of speech tagging, intent recognition or classification of any category you have in mind. Next to training, a small web application
    is included in the package to allow you to easily construct training data.
	"""
	
	homepage = "https://github.com/bnosac/crfsuite"
	cran = "crfsuite" 

	version("0.4.2", md5="f4af6a55b57e1656ced0c787d5857894")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-data-table@1.9.6:", type=("build", "run"))
