# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAwsSignature(RPackage):
    """Generates version 2 and version 4 request signatures for Amazon Web Services ('AWS') <https://aws.amazon.com/> Application Programming Interfaces ('APIs') and provides a mechanism for retrieving credentials from environment variables, 'AWS' credentials files, and 'EC2' instance metadata."""

    homepage = "https://github.com/cloudyr/aws.signature"
    cran = "aws.signature"

    version("0.6.0", sha256="f7fe4f686979be21e5a8ba7ae11f0fade4f5aaf4e98063b5349ee0962dbb9496")
    version("0.5.2", sha256="aef92b7a5c49b2bca1afdcbfc464440aabeabcdc95da170ac5c71a2adc5b716a")
    version("0.5.0", sha256="15dc4162dd0c4027fef109de6651adbe6e6bfaceb97e485adb37664cd12442c6")
    version("0.4.4", sha256="ccd76f4b4152433828cffd58cc3b8a4eb90df4bf17ee5c535139a246d5a984a3")
    version("0.4.1", sha256="3255c8e88e8a7ce51ffc6032e21c3a3398b7654d79e83d5d5b6310f3b8048d24")
    version("0.3.5", sha256="137a7274fab2924a3c6b9cc3e5c38714c2761d2531af076bf3b17443766f5fc6")
    version("0.3.2", sha256="983f32ae8f0ccb612a8bab569fc21232f114ea4d004b2be6c4848283fa7a6385")
    version("0.2.9", sha256="5f11ff63203733d7bae0d8cb8ca2ed0a2ee03f0cdfa5407466062314baf98f13")
    version("0.2.6", sha256="6e2ade0758e78e6075ce3aa7ceb7da6b32ba8a00f7140d480a95555afd14a931")
    version("0.2.5", sha256="68286fcd9c7e9434664c0544043651537580c0a1e4b2dc617a368a3499a39cd7")
    version("0.2.2", sha256="c7bd59ffafe3579c6cd5802fdcc66c1cfc635401930d57b6b75d8c8ee124cef2")
    version("0.2.0", sha256="4f01333b1d3d3ed996170e01e32fe1848f970bf2e42c1e938d011ee136ec4c3c")

    depends_on("r-digest", type=("build", "run"))
    depends_on("r-base64enc", type=("build", "run"))
    depends_on("r-testthat", type=("build", "run"))
    depends_on("r-aws-ec2metadata", type=("build", "run"))
