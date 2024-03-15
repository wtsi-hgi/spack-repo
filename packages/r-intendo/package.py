# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntendo(RPackage):
	"""A Group of Fun Datasets of Various Sizes and Differing Levels of
Quality

	Four datasets are provided here from the 'Intendo' game
    'Super Jetroid'. It is data from the 2015 year of operation and it comprises
    a revenue table ('all_revenue'), a daily users table ('users_daily'), a user
    summary table ('user_summary'), and a table with data on all user sessions
    ('all_sessions'). These core datasets come in different sizes, and, each of
    them has a variant that was intentionally made faulty (totally riddled with
    errors and inconsistencies). This suite of tables is useful for testing with
    packages that focus on data validation and data documentation.
	"""
	
	cran = "intendo" 

	version("0.1.1", md5="db98be815b2c62cb2da519106eda9548")

	depends_on("r@3.5:", type=("build", "run"))
