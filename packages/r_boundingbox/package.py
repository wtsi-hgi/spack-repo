# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBoundingbox(RPackage):
	"""Create a Bounding Box in an Image

	Generate ground truth cases for object localization algorithms. 
    Cycle through a list of images, select points around which to generate bounding 
    boxes and assign classifiers. Output the coordinates, and images annotated with 
    boxes and labels. For an example study that uses bounding boxes for image 
    localization and classification see Ibrahim, Badr, Abdallah, and Eissa (2012)
    "Bounding Box Object Localization Based on Image Superpixelization"
    <doi:10.1016/j.procs.2012.09.119>.
	"""
	
	homepage = "<https://github.com/stomperusa/boundingbox>"
	cran = "boundingbox" 

	version("1.0.1", md5="08b6cef1f0e7a9270a2cf27630e3871a")

	depends_on("r-imager", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
