# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInspire(RPackage):
	"""Inferring Shared Modules from Multiple Gene Expression Datasets
with Partially Overlapping Gene Sets

	A method to infer modules of co-expressed genes and the
    dependencies among the modules from multiple expression datasets that may
    contain different sets of genes. Please refer to: Extracting a low-dimensional
    description of multiple gene expression datasets reveals a potential driver for
    tumor-associated stroma in ovarian cancer, Safiye Celik, Benjamin A. Logsdon,
    Stephanie Battle, Charles W. Drescher, Mara Rendi, R. David Hawkins and Su-In
    Lee (2016) <DOI:10.1186/s13073-016-0319-7>.
	"""
	
	homepage = "inspire.cs.washington.edu"
	cran = "INSPIRE" 

	version("1.5", md5="2403e519df37b38019414a7318c1d985")

	depends_on("r-missmda", type=("build", "run"))
