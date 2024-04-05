# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTciu(RPackage):
	"""Spacekime Analytics, Time Complexity and Inferential Uncertainty

	Provide the core functionality to transform longitudinal data to
    complex-time (kime) data using analytic and numerical techniques, visualize the original 
    time-series and reconstructed kime-surfaces, perform model based (e.g., tensor-linear regression)
    and model-free classification and clustering methods in the book Dinov, ID and Velev, MV. (2021)
    "Data Science: Time Complexity, Inferential Uncertainty, and Spacekime Analytics", De Gruyter STEM Series,
    ISBN 978-3-11-069780-3. <https://www.degruyter.com/view/title/576646>.
    The package includes 18 core functions which can be separated into three groups.
    1) draw longitudinal data, such as Functional magnetic resonance imaging(fMRI) time-series, and forecast or transform the time-series data.
    2) simulate real-valued time-series data, e.g., fMRI time-courses, detect the activated areas,
    report the corresponding p-values, and visualize the p-values in the 3D brain space.
    3) Laplace transform and kimesurface reconstructions of the fMRI data.
	"""
	
	homepage = "https://github.com/SOCR/TCIU"
	cran = "TCIU" 

	version("1.2.5", md5="36955d3bb0f03e782d21b399a886e2f0")
	version("1.2.4", md5="e90f03cd6536c85ceaf1ee9cf028798b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-fancycut", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-icsnp", type=("build", "run"))
	depends_on("r-rrcov", type=("build", "run"))
	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-fmri", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-extradistr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-spatstat-explore", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-multiwayregression", type=("build", "run"))
