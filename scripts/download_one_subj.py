

import boto3
import csv
import botocore

from pathlib import Path

with open("data/1200_ids.csv","r") as f:
    hcp1200_ids = [line[0] for line in csv.reader(f)]

with open("data/7T_ids.csv","r") as f:
    hcp7T_ids = [line[0] for line in csv.reader(f)]


hcp_intersect = [subj for subj in hcp1200_ids if subj in hcp7T_ids]

##JUST ONE
hcp1200_ids = [hcp_intersect[0]]
hcp7T_ids = [hcp_intersect[0]]

session = boto3.Session(profile_name="hcp")
s3 = session.client('s3')

for subj in hcp1200_ids:
    print(subj)

    subj_path = f"data/downloaded/{subj}/hcp1200/"
    Path(subj_path).mkdir(parents=True, exist_ok=True)

    try:
        with open(f"{subj_path}/T1w_acpc_dc.nii.gz","wb") as f:
            s3.download_fileobj("hcp-openaccess",f"HCP_1200/{subj}/T1w/T1w_acpc_dc.nii.gz",f)
        with open(f"{subj_path}/T1w_acpc_dc_restore.nii.gz","wb") as f:
            s3.download_fileobj("hcp-openaccess",f"HCP_1200/{subj}/T1w/T1w_acpc_dc_restore.nii.gz",f)
        with open(f"{subj_path}/T1w_acpc_dc_restore_1.25.nii.gz","wb") as f:
            s3.download_fileobj("hcp-openaccess",f"HCP_1200/{subj}/T1w/T1w_acpc_dc_restore_1.25.nii.gz",f)
        with open(f"{subj_path}/T1w_acpc_dc_restore_brain.nii.gz","wb") as f:
            s3.download_fileobj("hcp-openaccess",f"HCP_1200/{subj}/T1w/T1w_acpc_dc_restore_brain.nii.gz",f)

    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            continue
        else:
            raise e


    try:
        with open(f"{subj_path}/bvals","wb") as f:
            s3.download_fileobj("hcp-openaccess",f"HCP_1200/{subj}/T1w/Diffusion/bvals",f)
        with open(f"{subj_path}/bvecs","wb") as f:
            s3.download_fileobj("hcp-openaccess",f"HCP_1200/{subj}/T1w/Diffusion/bvecs",f)
        with open(f"{subj_path}/data.nii.gz","wb") as f:
            s3.download_fileobj("hcp-openaccess",f"HCP_1200/{subj}/T1w/Diffusion/data.nii.gz",f)
        with open(f"{subj_path}/grad_dev.nii.gz","wb") as f:
            s3.download_fileobj("hcp-openaccess",f"HCP_1200/{subj}/T1w/Diffusion/grad_dev.nii.gz",f)
        with open(f"{subj_path}/wmparc.nii.gz","wb") as f:
            s3.download_fileobj("hcp-openaccess",f"HCP_1200/{subj}/T1w/wmparc.nii.gz",f)

    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            continue
        else:
            raise e

for subj in hcp7T_ids:
    continue
    print(subj)

    try:
        s3.Object("hcp-openaccess",f"HCP_1200/{subj}/T1w/Diffusion_7T/bvals").load()
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
          continue
        else:
          raise e

    subj_path = f"data/downloaded/{subj}/hcp7T/"
    Path(subj_path).mkdir(parents=True, exist_ok=True)

    try:
        with open(f"{subj_path}/bvals","wb") as f:
            s3.download_fileobj("hcp-openaccess",f"HCP_1200/{subj}/T1w/Diffusion_7T/bvals",f)
        with open(f"{subj_path}/bvecs","wb") as f:
            s3.download_fileobj("hcp-openaccess",f"HCP_1200/{subj}/T1w/Diffusion_7T/bvecs",f)
        with open(f"{subj_path}/data.nii.gz","wb") as f:
            s3.download_fileobj("hcp-openaccess",f"HCP_1200/{subj}/T1w/Diffusion_7T/data.nii.gz",f)
        with open(f"{subj_path}/grad_dev.nii.gz","wb") as f:
            s3.download_fileobj("hcp-openaccess",f"HCP_1200/{subj}/T1w/Diffusion_7T/grad_dev.nii.gz",f)
        ##with open(f"{subj_path}/wmparc.nii.gz","wb") as f:
        ##  s3.download_fileobj("hcp-openaccess",f"HCP_1200/{subj}/T1w/wmparc.nii.gz",f)

    except botocore.exceptions.ClientError as e:

        if e.response['Error']['Code'] == "404":
            continue
        else:
            raise e






