requirements:
	pip install --upgrade pip &&\
		pip install -r requirements.txt &&\
			touch .env

run:
	streamlit run app.py