# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClustercrit(RPackage):
	"""Clustering Indices

	Package providing functions for computing a collection of clustering validation or quality criteria and partition comparison indices.
	"""
	
	homepage = "https://gitlab.com/iagogv/clusterCrit"
	cran = "clusterCrit" 

	version("1.3.0", md5="29e3fc066da888a43bfedb048d932e12")

