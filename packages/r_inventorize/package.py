# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInventorize(RPackage):
	"""Inventory Analytics, Pricing and Markdowns

	Simulate inventory policies with and without forecasting, facilitate inventory analysis calculations such as  stock levels and re-order points,pricing and promotions calculations. 
  The package includes calculations of inventory metrics, stock-out calculations and ABC analysis calculations.
    The package includes revenue management techniques such as Multi-product optimization,logit and polynomial model optimization.
  The functions are referenced from :
  1-Harris, Ford W. (1913). "How many parts to make at once". Factory, The Magazine of Management. <isbn10: 135–136, 152>.
  2- Nahmias, S. Production and Operations Analysis. McGraw-Hill International Edition. <isbn: 0-07- 2231265-3. Chapter 4>.
  3-Silver, E.A., Pyke, D.F., Peterson, R. Inventory Management and Production Planning and Scheduling. <isbn: 978-0471119470>. 
  4-Ballou, R.H. Business Logistics Management. <isbn: 978-0130661845>. Chapter 9.
  5-MIT Micromasters Program. 
  6- Columbia University  course for supply and demand analysis.
  8- Price Elasticity of Demand MATH 104,Mark Mac Lean (with assistance from Patrick Chan) 2011W
  For further details or correspondence :<www.linkedin.com/in/haythamomar>, <www.rescaleanalytics.com>.
	"""
	
	cran = "inventorize" 

	version("1.1.1", md5="73b565d22159d9514d048b639812eaef")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
