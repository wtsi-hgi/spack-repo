# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFreesurferformats(RPackage):
	"""Read and Write 'FreeSurfer' Neuroimaging File Formats

	Provides functions to read and write neuroimaging data in various file formats, with a focus on 'FreeSurfer' <http://freesurfer.net/> formats. This includes, but is not limited to, the following file formats: 1) MGH/MGZ format files, which can contain multi-dimensional images or other data. Typically they contain time-series of three-dimensional brain scans acquired by magnetic resonance imaging (MRI). They can also contain vertex-wise measures of surface morphometry data. The MGH format is named after the Massachusetts General Hospital, and the MGZ format is a compressed version of the same format. 2) 'FreeSurfer' morphometry data files in binary 'curv' format. These contain vertex-wise surface measures, i.e., one scalar value for each vertex of a brain surface mesh. These are typically values like the cortical thickness or brain surface area at each vertex. 3) Annotation file format. This contains a brain surface parcellation derived from a cortical atlas. 4) Surface file format. Contains a brain surface mesh, given by a list of vertices and a list of faces.
	"""
	
	homepage = "https://github.com/dfsp-spirit/freesurferformats"
	cran = "freesurferformats" 

	version("0.1.18", md5="1e43487c40ea9a0640f1602933cba43e")

	depends_on("r-pkgfilecache@0.1.1:", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
