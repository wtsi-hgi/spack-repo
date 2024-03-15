# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFolio(RPackage):
	"""Datasets for Teaching Archaeology and Paleontology

	Datasets for teaching quantitative approaches and modeling in
    archaeology and paleontology. This package provides several types of
    data related to broad topics (cultural evolution, radiocarbon dating,
    paleoenvironments, etc.), which can be used to illustrate statistical
    methods in the classroom (multivariate data analysis, compositional
    data analysis, diversity measurement, etc.).
	"""
	
	homepage = "https://packages.tesselle.org/folio/"
	cran = "folio" 

	version("1.4.0", md5="b4be76f3dfd0f0d0fc0fd5220af58c13")

	depends_on("r@2.10:", type=("build", "run"))
