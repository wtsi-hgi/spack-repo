# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBioimageioSpec(PythonPackage):
    """Contains specifications defined by the BioImage.IO community."""

    homepage = "https://github.com/bioimage-io/spec-bioimage-io"
    pypi = "bioimageio.spec/bioimageio.spec-0.4.9.post5.tar.gz"

    version("0.4.9.post5", sha256="1b8e20be79a0f7e78c8dc1a7a2984646d9bcaeb811386a45de0806fc7757cc46")

    depends_on("py-marshmallow-jsonschema", type=("build", "run"))
    depends_on("py-marshmallow-union", type=("build", "run"))
    depends_on("py-marshmallow@3.6.0:4.0", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-packaging@17.0:", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-ruamel-yaml", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-typer", type=("build", "run"))
    depends_on("py-typing-extensions", type=("build", "run"))
