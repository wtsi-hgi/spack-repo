# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCellregmap(PythonPackage):
    """Cellular Regulatory Map (CellRegMap) is a linear mixed model approach to perform multi-context eQTL mapping by leveraging single cell RNA sequencing (scRNA-seq) data. It is related to the previously proposed StructLMM but importantly it can account for sample structure, including population structure and repeated observations for the same samples, e.g., multiple cells for the same donor."""

    homepage = "https://github.com/limix/CellRegMap"
    pypi = "cellregmap/cellregmap-0.0.3.tar.gz"

    version("0.0.3", sha256="ac98cbe6972777eda79e9bef7de611a3d61f4f1aedef3b74a2916a0d3cb3fff4")

    depends_on("py-setuptools", type="build")
