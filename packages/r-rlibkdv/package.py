# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRlibkdv(RPackage):
	"""A Versatile Kernel Density Visualization Library for Geospatial
Analytics (Heatmap)

	Unlock the power of large-scale geospatial analysis, 
    quickly generate high-resolution kernel density visualizations, 
    supporting advanced analysis tasks such as bandwidth-tuning and spatiotemporal analysis. 
    Regardless of the size of your dataset, our library delivers efficient and accurate results.
    Tsz Nam Chan, Leong Hou U, Byron Choi, Jianliang Xu, Reynold Cheng (2023) <doi:10.1145/3555041.3589401>.
    Tsz Nam Chan, Rui Zang, Pak Lon Ip, Leong Hou U, Jianliang Xu (2023) <doi:10.1145/3555041.3589711>.
    Tsz Nam Chan, Leong Hou U, Byron Choi, Jianliang Xu (2022) <doi:10.1145/3514221.3517823>.
    Tsz Nam Chan, Pak Lon Ip, Kaiyan Zhao, Leong Hou U, Byron Choi, Jianliang Xu (2022) <doi:10.14778/3554821.3554855>.
    Tsz Nam Chan, Pak Lon Ip, Leong Hou U, Byron Choi, Jianliang Xu (2022) <doi:10.14778/3503585.3503591>.
    Tsz Nam Chan, Pak Lon Ip, Leong Hou U, Byron Choi, Jianliang Xu (2022) <doi:10.14778/3494124.3494135>.
    Tsz Nam Chan, Pak Lon Ip, Leong Hou U, Weng Hou Tong, Shivansh Mittal, Ye Li, Reynold Cheng (2021) <doi:10.14778/3476311.3476312>.
    Tsz Nam Chan, Zhe Li, Leong Hou U, Jianliang Xu, Reynold Cheng (2021) <doi:10.14778/3461535.3461540>.
    Tsz Nam Chan, Reynold Cheng, Man Lung Yiu (2020) <doi:10.1145/3318464.3380561>.
    Tsz Nam Chan, Leong Hou U, Reynold Cheng, Man Lung Yiu, Shivansh Mittal (2020) <doi:10.1109/TKDE.2020.3018376>.
    Tsz Nam Chan, Man Lung Yiu, Leong Hou U (2019) <doi:10.1109/ICDE.2019.00055>.
	"""
	
	homepage = "https://github.com/bojianzhu/Rlibkdv"
	cran = "Rlibkdv" 

	version("1.1", md5="47b6967c2f8bab3dda1153cd6542eb2e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
