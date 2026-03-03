# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-sigprofilerassignment
#
# You can edit this file again by typing:
#
#     spack edit py-sigprofilerassignment
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PySigprofilerassignment(PythonPackage):
    """SigProfilerAssignment enables assignment of previously known mutational signatures to individual samples and individual somatic mutations."""

    homepage = "https://github.com/AlexandrovLab/SigProfilerAssignment"

    url = "https://github.com/AlexandrovLab/SigProfilerAssignment/archive/refs/tags/v0.1.8.tar.gz"

    license("BSD-2-Clause")

    version(
        "0.1.8",
        sha256="fb68482e51d648a3d958a281d01cf5c8d7b8b56e4dca46c906a79efce0136fb1",
    )
    version(
        "0.1.7",
        sha256="4c2533379527d647b4908e29628f431c6011aaed58c74ec4adfee12dc8dc1d8c",
    )
    version(
        "0.1.6",
        sha256="42ff08e5d0641e8aab7e83400824befd10ba6a6aab9f4c54e51ab14830355dc6",
    )
    version(
        "0.1.5",
        sha256="de97059224f69bb82e075d34d2028f04d3315ca0a8b549585b5bd247c456ca8b",
    )
    version(
        "0.1.4",
        sha256="dc07bf34dbc5791dc1c2295de1d88b71935197036b693dc2078735c41aa7fe9f",
    )
    version(
        "0.1.3",
        sha256="8d71e1dd9a50d6b34fd6270ff61605f53d6cbb1816699b84bc4848d73fe440ec",
    )
    version(
        "0.1.2",
        sha256="9c4623891b31b2077584494b845494c54acd8c318f25ef7101262674136907d7",
    )
    version(
        "0.1.1",
        sha256="cda3b530cda9dbe28667bbb1320abc51bb584da426203a7ddfc50a9a32b8857e",
    )
    version(
        "0.1.0",
        sha256="f4323f4681a8efb4b3921004edcdfa79ab3200b9eb6965a2c7b4dde15667ac5b",
    )
    version(
        "0.0.33",
        sha256="972bc971f92dfeb4efd39000312b298efec8686dbf6e29f740d7b9ab98f43fdf",
    )

    depends_on("py-sigprofilermatrixgenerator", type=("build", "run"))

    depends_on("py-setuptools", type="build")
