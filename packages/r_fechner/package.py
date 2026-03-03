# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFechner(RPackage):
	"""Fechnerian Scaling of Discrete Object Sets

	Functions and example datasets for Fechnerian scaling of discrete
  object sets.  User can compute Fechnerian distances among objects representing
  subjective dissimilarities, and other related information.  See
  package?fechner for an overview.
	"""
	
	homepage = "http://www.meb.edu.tum.de"
	cran = "fechner" 

	version("1.0-3", md5="fe6e70ee040f0feae1ec88a97fdde76b")

	depends_on("r@3.3:", type=("build", "run"))
