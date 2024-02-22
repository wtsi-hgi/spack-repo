# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPreprocessrecordlinkage(RPackage):
	"""Preprocessing Record Linkage

	In this record linkage package, data preprocessing has been meticulously executed
  to cover a wide range of datasets, ensuring that variable names are standardized using synonyms. 
  This approach facilitates seamless data integration and analysis across various datasets. While users 
  have the flexibility to modify variable names, the system intelligently ensures that 
  changes are only permitted when they do not compromise data consistency or essential variable essence.
	"""
	
	cran = "PreProcessRecordLinkage" 

	version("1.0.1", md5="f6662d5ddb937cab4a23cbe98aa42e4c")

	depends_on("r-tm", type=("build", "run"))
	depends_on("r-syn", type=("build", "run"))
	depends_on("r-recordlinkage", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
