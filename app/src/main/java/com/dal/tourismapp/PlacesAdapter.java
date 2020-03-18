package com.dal.tourismapp;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import java.util.ArrayList;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

public class PlacesAdapter extends RecyclerView.Adapter<PlacesAdapter.MyViewHolder> {
    private ArrayList<String> mtitle;
    private ArrayList<String> mdesc;
    private ArrayList<String> motherInfo;
    private ArrayList<String> mImage;

    public static class MyViewHolder extends RecyclerView.ViewHolder {
        public TextView title;
        public TextView desc;
        public TextView other_info;
        public MyViewHolder(View v) {
            super(v);
            title = v.findViewById(R.id.title);
            desc = v.findViewById(R.id.desc);
            other_info = v.findViewById(R.id.other_info);
        }
    }
    public PlacesAdapter(ArrayList<String> titles, ArrayList<String> desc, ArrayList<String> other_info ) {

    mtitle = titles;
    mdesc = desc;
    motherInfo = other_info;
    }



    @Override
    public void onBindViewHolder(@NonNull PlacesAdapter.MyViewHolder holder, int position) {

        holder.title.setText(mtitle.get(position));
        holder.desc.setText(mdesc.get(position));
        holder.other_info.setText(motherInfo.get(position));
    }
    //creating my views
    @Override
    public  PlacesAdapter.MyViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        //create a new view
        View v =  LayoutInflater.from(parent.getContext()).inflate(R.layout.places_card, parent, false);

        MyViewHolder vh = new MyViewHolder(v);
        return vh;
    }

    @Override
    public int getItemCount() {
        return mdesc.size();
    }
}
