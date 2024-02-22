# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetagear(RPackage):
	"""Comprehensive Research Synthesis Tools for Systematic Reviews
and Meta-Analysis

	Functionalities for facilitating systematic reviews, data
    extractions, and meta-analyses. It includes a GUI (graphical user interface)
    to help screen the abstracts and titles of bibliographic data; tools to assign
    screening effort across multiple collaborators/reviewers and to assess inter-
    reviewer reliability; tools to help automate the download and retrieval of
    journal PDF articles from online databases; figure and image extractions 
    from PDFs; web scraping of citations; automated and manual data extraction 
    from scatter-plot and bar-plot images; PRISMA (Preferred Reporting Items for
    Systematic Reviews and Meta-Analyses) flow diagrams; simple imputation tools
    to fill gaps in incomplete or missing study parameters; generation of random
    effects sizes for Hedges' d, log response ratio, odds ratio, and correlation
    coefficients for Monte Carlo experiments; covariance equations for modelling
    dependencies among multiple effect sizes (e.g., effect sizes with a common
    control); and finally summaries that replicate analyses and outputs from 
    widely used but no longer updated meta-analysis software (i.e., metawin).
	Funding for this package was supported by National Science Foundation (NSF) 
	grants DBI-1262545 and DEB-1451031. CITE: Lajeunesse, M.J. (2016) 
	Facilitating systematic reviews, data extraction and meta-analysis with the 
	metagear package for R. Methods in Ecology and Evolution 7, 323-330 
	<doi:10.1111/2041-210X.12472>.
	"""
	
	homepage = "http://lajeunesse.myweb.usf.edu/"
	cran = "metagear" 

	version("0.7", md5="783c1dfff1dda17162fb3f571090e743")

	depends_on("r@3.3.2:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-metafor@1.9.9:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("tcl", type=("build", "link", "run"))
	depends_on("tk", type=("build", "link", "run"))
