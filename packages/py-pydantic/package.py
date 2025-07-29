# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyPydantic(PythonPackage):
    """Data validation and settings management using Python type hinting."""

    homepage = "https://github.com/pydantic/pydantic"
    pypi = "pydantic/pydantic-1.8.2.tar.gz"

    license("MIT")

    version("2.10.1", sha256="a4daca2dc0aa429555e0656d6bf94873a7dc5f54ee42b1f5873d666fb3f35560")
    version("2.7.4", sha256="0c84efd9548d545f63ac0060c1e4d39bb9b14db8b3c0652338aecc07b5adec52")
    version("2.1.0", sha256="80a67e716158c813c9a6c0ce936ee24577e9fbd7453d159fc79850747a9aaa76")
    version("2.0.1", sha256="041945a6c75f2451a343674ec7d220cb7e207884fb06aaf2c16b6d0bfaf2bc39")
    version("2.0.2", sha256="b802f5245b8576315fe619e5989fd083448fa1258638ef9dac301ca60878396d")
    version("1.10.19", sha256="fea36c2065b7a1d28c6819cc2e93387b43dd5d3cf5a1e82d8132ee23f36d1f10")
    version("1.10.9", sha256="95c70da2cd3b6ddf3b9645ecaa8d98f3d80c606624b6d245558d202cd23ea3be")
    version("1.10.2", sha256="91b8e218852ef6007c2b98cd861601c6a09f1aa32bbbb74fab5b1c33d4a1e410")
    version("1.9.2", sha256="8cb0bc509bfb71305d7a59d00163d5f9fc4530f0881ea32c74ff4f74c85f3d3d")
    version("1.8.2", sha256="26464e57ccaafe72b7ad156fdaa4e9b9ef051f69e175dbbb463283000c05ab7b")

    variant("dotenv", default=False, description="Install requirements for pydantic.dotenv")

    depends_on("py-setuptools", type="build", when="@1")
    depends_on("py-hatchling", type="build", when="@2")
    depends_on("py-hatch-fancy-pypi-readme", when="@2:", type="build")
    depends_on("py-typing-extensions@4.12.2:", when="@2.10:", type=("build", "run"))
    depends_on("py-typing-extensions@4.6.1:", when="@2.7.1:", type=("build", "run"))
    depends_on("py-typing-extensions@4.2:", when="@1.10.9:", type=("build", "run"))
    depends_on("py-typing-extensions@4.1:", when="@1.10:", type=("build", "run"))
    depends_on("py-typing-extensions@3.7.4.3:", type=("build", "run"))
    depends_on("py-annotated-types@0.6:", type=("build", "run"), when="@2.10:")
    depends_on("py-annotated-types@0.4.0:", type=("build", "run"), when="@2.7.4:")
    depends_on("py-pydantic-core@2.27.1", type=("build", "run"), when="@2.10.1")
    depends_on("py-pydantic-core@2.18.4", type=("build", "run"), when="@2.7.4")
    depends_on("py-python-dotenv@0.10.4:", when="@1 +dotenv", type=("build", "run"))
    depends_on("py-pydantic-core", when="@2:", type=("build", "run"))
    depends_on("py-annotated-types@0.4.0:", when="@2:", type=("build", "run"))
    depends_on("py-pydantic-core@=2.0.2", when="@2.0.1", type=("build", "run"))

    # https://github.com/pydantic/pydantic/pull/9612
    conflicts("python@3.12.4:", when="@:1.10.15")
