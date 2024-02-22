# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPartitionmetric(RPackage):
	"""Compute a distance metric between two partitions of a set

	partitionMetric computes a distance between two partitions
        of a set.
	"""
	
	cran = "partitionMetric" 

	version("1.1", md5="32196486df30290c06a05d992e4ab2cb")

	depends_on("r@2.10.1:", type=("build", "run"))
