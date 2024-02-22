# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKhroma(RPackage):
	"""Colour Schemes for Scientific Data Visualization

	Color schemes ready for each type of data (qualitative,
    diverging or sequential), with colors that are distinct for all
    people, including color-blind readers. This package provides an
    implementation of Paul Tol (2018) and Fabio Crameri (2018)
    <doi:10.5194/gmd-11-2541-2018> color schemes for use with 'graphics'
    or 'ggplot2'. It provides tools to simulate color-blindness and to
    test how well the colors of any palette are identifiable. Several
    scientific thematic schemes (geologic timescale, land cover, FAO
    soils, etc.) are also implemented.
	"""
	
	homepage = "https://packages.tesselle.org/khroma/"
	cran = "khroma" 

	version("1.12.0", md5="648547bfde4a1939b0066b281efaeb3a")

	depends_on("r@3.5:", type=("build", "run"))
