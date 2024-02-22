# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvacluster(RPackage):
	"""Evaluation Clustering Methods for Disease Subtypes Diagnosis

	Contains a set of clustering methods and evaluation metrics to select the best number of the clusters based on clustering stability. Two references describe the methodology: Fahimeh Nezhadmoghadam, and Jose Tamez-Pena (2021)<doi:10.1016/j.compbiomed.2021.104753>, and Fahimeh Nezhadmoghadam, et al.(2021)<doi:10.2174/1567205018666210831145825>.
	"""
	
	cran = "Evacluster" 

	version("0.1.0", md5="f1dd882a6f97729e25e41dfca96f3a3c")

