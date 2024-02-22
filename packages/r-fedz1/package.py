# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFedz1(RPackage):
	"""An Easier Access to Financial Accounts of the United States(Z.1)

	Flow of funds are financial accounts that are provided by Federal Reserve quarterly. The package contains all
    datasets <https://www.federalreserve.gov/datadownload/Choose.aspx?rel=z1>, tables <https://www.federalreserve.gov/apps/fof/FOFTables.aspx> 
    and descriptions <https://www.federalreserve.gov/apps/fof/Guide/z1_tables_description.pdf> with functions to understand series <https://www.federalreserve.gov/apps/fof/SeriesStructure.aspx> and explore them. 
	"""
	
	homepage = "https://github.com/shaf1430/fedz1"
	cran = "fedz1" 

	version("0.1.0", md5="2a795a36a5c4a36fd9c72f22cb3655d7", url="https://cran.r-project.org/src/contrib/fedz1_0.1.0.tar.gz")

	depends_on("r@2.10:", type=("build", "run"))
